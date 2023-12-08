ts_out_folder=AAL116ts_run1
num_parcels=116
atlas_file=../../../../../Codes/AAL_space_116.nii.gz



mkdir ../$ts_out_folder
func_file=filtered_func_data_standard.nii.gz

cd ../fapia_derivatives
RUNDIR='run-1'
for d in */ ; do
    echo "$d"
    cd $d/func/$RUNDIR/+++.feat/

    mkdir ../../../../../$ts_out_folder/$d
    for (( i=1; i<=$num_parcels; i++));do
        ii=`zeropad $i 3`   # this is just to make sure the output is in the correct order
        fslmaths $atlas_file -thr $i -uthr $i tmp_mask
        fslmeants -i $func_file -m tmp_mask  > ../../../../../$ts_out_folder/$d/out_$ii.txt
    done

    pwd
    cd ../../../../
done
