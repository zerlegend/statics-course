# Review checklist (before publishing)

These items need a person. Tick them off and delete this file when done.

## Check on a real device
- [ ] Open the built site (`npm run docs:preview`) in a desktop browser and on a phone.
- [ ] Check that all formulas render, in light and dark mode.
- [ ] Tap a figure on the phone: it should zoom and close again.
- [ ] Try the Quick Quiz on each chapter.
- [ ] Print one chapter and the Formula Sheet (print preview): menus should be hidden.

## Placeholders to fill
- [ ] Telegram channel link on the Instructors page.
- [ ] Official grading scale in `docs/syllabus/assessment.md` (currently a placeholder).
- [ ] Official CLO statements in `docs/syllabus/learning-outcomes.md`.
- [ ] Confirm the licence on `docs/resources/licence.md` (CC BY-NC-SA 4.0 proposed).

## Second-person check of the content
Ask a colleague or a strong student to work these independently and compare:
- [ ] Chapter 1: Examples 1.1–1.4 and Tutorial Problems 1–5
- [ ] Chapter 2: Examples 2.1–2.4 and Tutorial Problems 1–6
- [ ] Chapter 3: Examples 3.1–3.4 and Tutorial Problems 1–7
- [ ] Chapter 4: Examples 4.1–4.4 and Tutorial Problems 1–7
- [ ] Chapter 5: Examples 5.1–5.4 and Tutorial Problems 1–6
- [ ] Chapter 6: Examples 6.1–6.4 and Tutorial Problems 1–7
- [ ] Chapter 7: Examples 7.1–7.4 and Tutorial Problems 1–6
- [ ] Real-world examples: the factor of safety (Ex 5.4) and ladder angle (Ex 7.4) comments against your local code and site-safety rules.

## Hosting
- [ ] Repository is named `statics-course` (or change `base` in `docs/.vitepress/config.js`).
- [ ] `package-lock.json` is committed (run `npm install` once).
- [ ] Settings → Pages → Source is **GitHub Actions**.
- [ ] The first deploy ran successfully (Actions tab).

## Releasing solutions
- [ ] Set `solutionsPublished = true` in `docs/.vitepress/config.js` when you want to release the solution pages, then push.
