rm $2
for f in $1/*
do
  echo '\n|begin|\n' >> $2
  cat "$f" >> $2
  echo '\n|end|\n' >> $2
done
