import os
import subprocess

def test_pipeline_execution():
<<<<<<< HEAD
    
    result = subprocess.run(["python", "project3.py"], capture_output=True, text=True)
    
    
    assert result.returncode == 0, f"Pipeline execution failed: {result.stderr}"
    
    
=======
   
    result = subprocess.run(["python", "project3.py"], capture_output=True, text=True)
    
   
    assert result.returncode == 0, f"Pipeline execution failed: {result.stderr}"
    
   
>>>>>>> 4f4ca2bb6ad103489ff3749d4be74c65fbbbe5b6
    output_file = "output_combined_data.csv"
    assert os.path.exists(output_file), f"Output file '{output_file}' does not exist"
    
    
    with open(output_file, 'r') as f:
        lines = f.readlines()
        assert len(lines) > 1, "Output file is empty or contains only headers"

    print("System test passed successfully!")
