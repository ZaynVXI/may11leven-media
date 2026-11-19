# May11Leven document system

Invoice, proposal and contract on A4. The structure comes from the editorial set in `brand/refs/documents/`: a label and value header grid, one oversized title word, hairlines and a lot of air. What makes it ours is the 11 mark and wordmark, Inter Tight, Plex Mono for every figure and reference, and Infrared used only on the mark and the step numbers.

## Use
1. Copy `sample.json`, then fill in the client, lines and dates. Anything in [square brackets] is a placeholder. These are tinted in the output so none slip through.
2. Run `python3 build.py`. It writes the PDFs and page previews to `out/`.
3. Numbering: M11-INV-0001, M11-PRO-0001, M11-CON-0001, counting up per type.

## Before the first real use (Zayn)
- Fill in the studio's legal name, address and tax ID, and the bank details. These are kept out of the repo. Add them only to the copy you send.
- Invoices and contracts need an issue date by law. That is the one place a date appears.
- The contract text is a plain-English starting point. Have a lawyer check it for your country before signing anything.
