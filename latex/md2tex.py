"""Minimal Markdown -> LaTeX for the plan files: headings, paragraphs, '- ' and 'N. ' lists, **bold**, `code`.
Text is kept word for word; only markup is converted."""
import re, sys
def esc(t):
    out=[]
    for ch in t:
        out.append({'\\':r'\textbackslash{}','%':r'\%','_':r'\_','&':r'\&','#':r'\#','$':r'\$','{':r'\{','}':r'\}',
                    '~':r'\textasciitilde{}','^':r'\textasciicircum{}','<':r'\textless{}','>':r'\textgreater{}'}.get(ch,ch))
    return ''.join(out)
def inline(t):
    codes=[]
    def keep(m):
        codes.append(r'\texttt{'+esc(m.group(1))+'}'); return '\x00%d\x01'%(len(codes)-1)
    t=re.sub(r'`([^`]*)`',keep,t)
    e=esc(t); e=re.sub(r'\*\*(.+?)\*\*',r'\\textbf{\1}',e)
    return re.sub('\x00(\\d+)\x01',lambda m:codes[int(m.group(1))],e)
def convert(lines, level_offset):
    out=[]; para=[]; lst=None; item=None
    def flush_para():
        nonlocal para
        if para: out.append(inline(' '.join(para))+'\n'); para=[]
    def flush_item():
        nonlocal item
        if item is not None: out.append(r'\item '+inline(' '.join(item))); item=None
    def close_list():
        nonlocal lst
        flush_item()
        if lst: out.append(r'\end{%s}'%lst+'\n'); lst=None
    for raw in lines:
        l=raw.rstrip('\n')
        m=re.match(r'^(#+)\s+(.*)',l)
        if m:
            flush_para(); close_list()
            lv=len(m.group(1))+level_offset
            cmd={1:'section',2:'subsection',3:'subsubsection'}.get(lv,'paragraph')
            out.append('\\%s*{%s}'%(cmd,inline(m.group(2)))); continue
        if not l.strip():
            flush_para(); close_list(); continue
        mb=re.match(r'^- (.*)',l); mn=re.match(r'^(\d+)\. (.*)',l)
        if mb or mn:
            flush_para(); kind='itemize' if mb else 'enumerate'
            if lst!=kind:
                close_list(); start=int(mn.group(1)) if mn else 1
                out.append(r'\begin{%s}'%kind+('[start=%d]'%start if mn and start!=1 else '')); lst=kind
            flush_item(); item=[(mb or mn).group(1 if mb else 2)]; continue
        if item is not None and re.match(r'^\s+\S',l):
            item.append(l.strip()); continue
        close_list(); para.append(l.strip())
    flush_para(); close_list()
    return '\n'.join(out)+'\n'
src,dst,off=sys.argv[1],sys.argv[2],int(sys.argv[3])
open(dst,'w').write(convert(open(src,encoding='utf-8').readlines(),off))
