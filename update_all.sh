
date=$(date)
python3 update_npr.py;
python3 slate.py;
python3 fivethirtyeight.py;
python3 daily_update.py;
outdir="output_{$date}"

./stitch npr_transcripts ${outdir}/npr_all
./stitch slate_transcripts ${outdir}/slate_all
./stitch fivethirtyeight_transcripts ${outdir}/fivethirtyeight_all
./stitch daily_transcripts ${outdir}/daily_all

cat ${outdir}/*_all >> ${outdir}/working

