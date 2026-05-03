# BISProject

## Run Instructions

1. Install dependencies:
pip install -r requirements.txt

2. Run inference:
python inference.py --input public_test_set.json --output results.json

3. Evaluate:
python eval_script.py --results results.json