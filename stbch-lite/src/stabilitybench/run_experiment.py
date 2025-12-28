import uuid
import datetime
import json
import pathlib


prompt_file_path = pathlib.Path("stbch-lite") / "prompts" / "prompts.jsonl"


with prompt_file_path.open("r") as f:
    prompts = [json.loads(line) for line in f.readlines()]

prompt = prompts[0]["prompt"]  # Select the first prompt for this example

N =  5 # Number of dummy outputs to generate
dummy_output_ = [f"output {i}" for i in range(1,N + 1)]

run = {"run_id": str(uuid.uuid4()),
       "timestamp": str(datetime.datetime.now()), 
       "prompt": prompt, 
       "model": "dummy_model", 
       "gen_parameters": {"temperature": 0.7, "max_tokens": 150}, 
       "metrics": {"latency": 0.123, "throughput": 8.1},
       "outputs": dummy_output_}


output_file_path = pathlib.Path("stbch-lite")/ "runs" / f"run_{run['run_id']}.json"

with output_file_path.open("w") as f:
    json.dump(run, f, indent=4)

print(f"Experiment run saved to {output_file_path}")

