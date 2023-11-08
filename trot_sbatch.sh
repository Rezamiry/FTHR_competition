#!/bin/bash

#SBATCH --mail-user=rm21zx@brocku.ca
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE
#SBATCH --mail-type=ALL

#SBATCH --job-name=6
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=64000M
#SBATCH --ntasks=1
#SBATCH --time=0-2:00:00
#SBATCH --nodes=1
start=$(date +%s)
run=$1
echo $run

module load StdEnv/2020 cuda cudnn
module load python/3.10.2
source ~/jupyter_py3/bin/activate

cd ~/projects/def-tianyu/rezmiry/trot_racing/
python -u $run.py
end=$(date +%s)
echo "Elapsed Time: $(($end-$start)) seconds"