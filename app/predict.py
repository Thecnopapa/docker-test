print(" * Starting predict.py...")

print(" * Loading imports...")
from werkzeug.utils import secure_filename
import sys, os, datetime, json, shutil, stat
from bioiain.machine.flows import predict


print(" * Copying FoldSeek...")
fs_path = "./tools/foldseek"
os.makedirs("./tools", exist_ok=True)
shutil.copy('/misc/foldseek', fs_path) 

os.chmod(fs_path, stat.S_IRWXU )
print(" * Foldseek bin:", fs_path)
assert os.path.exists(fs_path)


JOBID = os.environ.get("JOBID", None)
print(" * JOBID:", JOBID)

def main():
    print(f" * Starting Job {JOBID} ...")

    #job_info = predict(file_path=file_path, model_data_path=data_path, chain_id=chain, pred_folder="/predictions", use_temp=False, force=True, timestamp=job_id, with_foldseek=False, foldseek_cmd=fs_path, download_folder="/misc/predict/.models")

    print(f"Job {JOBID} completed!")




if __name__ == "__main__":
    print(" * Executing main() ...")
    main()
    print(" * Execution complete!")

