
cd data
rm -rf *
mkdir eds mrs
cd ../wsi-src
./create-index -f mrs -o /Users/ar/work/text-entailment/data/mrs /Users/ar/work/text-entailment/export
./create-index -f eds -o /Users/ar/work/text-entailment/data/eds /Users/ar/work/text-entailment/export
