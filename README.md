# Pre-specified analysis plans

Analysis plans for the paper *How fragile a deep lung-nodule detector appears depends on the texture of simulated
noise: a paired evaluation of training-time augmentation* by Mahmoud S. Yaseen and Ali Okatan (Software Engineering
Department, Istanbul Aydin University, Istanbul, Türkiye). Correspondence: mahmoudyaseen@stu.aydin.edu.tr

Code: https://github.com/Mahmoudyasen/lung-nodule-detector-robustness

## Contents

| File | What it is |
|---|---|
| `analysis_plans.pdf` | All three plans in one document: Part A (F1–F3), Part B (F4, noise texture), Part C (F5–F7, second seed), each with the notes written afterwards. |
| `plans_original/` | The original plan files. Parts B and C of the PDF reproduce them word for word. |
| `SHA256SUMS` | SHA-256 of the files in `plans_original/`. |
| `hash_records/` | The two hash record files written before the data of each plan were generated (copied unchanged; the recording time is written inside each file). |
| `latex/` | LaTeX source of the PDF (`pdflatex analysis_plans.tex`, twice). `md2tex.py` converts the Markdown files into `gen_*.tex`. |

## Checking the hashes

```
cd plans_original && sha256sum -c ../SHA256SUMS
```

The hashes of the two plan files were recorded before any of their data were generated:

| Plan | SHA-256 | Recorded (UTC+3) |
|---|---|---|
| `texture_test_prespec.md` | `7cf2ba56f78e1eb39c2d75cbf0b8d308b4141a13430300e129748ee264162da4` | 2 Nov 2026, 16:58:38 |
| `review_prespec.md` | `edc7a8be4f3de8df1a1e0f5607220ab0be36fa71499d205c78c918c7384b99fe` | 2 Nov 2026, 20:31:58 |

The record files were written next to the analysis outputs (`analysis/p2_texture/PRESPEC_SHA256.txt` and
`analysis/p2_review/PRESPEC_SHA256.txt`); copies are in `hash_records/`. The texture plan was originally named `p2_texture_prespec.md`
and the review plan `p2_review_prespec.md`; the hashes cover the file contents, so the renaming does not affect them.
The record times are file times on the first author's computer, not external time stamps.

The `*_NOTES.md` files were written after the data were seen; they list deviations and added analyses, which the paper
labels as not pre-specified. Part A (F1–F3) was kept in the first author's project progress document; its committed versions and their
times are given in Part A of the PDF.

## Licence

[To be chosen by the author, e.g. CC BY 4.0 for the documents.]
