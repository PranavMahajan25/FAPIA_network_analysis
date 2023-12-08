cd ../fapia_derivatives
RUNPREFIX='run-'
for d in */ ; do
    echo "$d"
    cd $d/func/
    RUNNUM=0
    # for (( j=1; j<=4; j++));do
    #     RUNNUM=$(($RUNNUM+1))
    #     RUNDIR="$RUNPREFIX$RUNNUM"
    #     cd $RUNDIR/+++.feat/
    #     pwd
    #     flirt -in filtered_func_data.nii.gz -ref reg/highres.nii.gz -out filtered_func_data_highres.nii.gz -init reg/example_func2highres.mat -applyxfm
    #     flirt -in filtered_func_data_highres.nii.gz -ref reg/standard.nii.gz -out filtered_func_data_standard.nii.gz -init reg/highres2standard.mat -applyxfm
    #     cd ../../
    # done
    
   
    RUNDIR='run-3'
    cd $RUNDIR/+++.feat/
    flirt -in filtered_func_data.nii.gz -ref reg/highres.nii.gz -out filtered_func_data_highres.nii.gz -init reg/example_func2highres.mat -applyxfm
    flirt -in filtered_func_data_highres.nii.gz -ref reg/standard.nii.gz -out filtered_func_data_standard.nii.gz -init reg/highres2standard.mat -applyxfm
    pwd
    cd ../../
    
    cd ../../
done
