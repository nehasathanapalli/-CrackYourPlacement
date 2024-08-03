void sortColours(int n){
    int count, nums[],n;

    for (int i = 0; i <n; i++){
        if(nums[i] == 0)
            count0++;
        if(nums[i] == 1)
            count1++;
        if(nums[i] == 2)
            count2++;
    }
    int i=0;
    while(count0>0){
        nums[i++] = 0;
        count0--;
    }
    while(count1>0){
        nums[i++] = 1;
        count1--;
    }
    while(count2>0){
        nums[i++] = 2;
        count2--;
    }
}
