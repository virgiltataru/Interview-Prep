#here we want to partition an array into 2 arrays with equal sumsself.
#just look for a subarray with sum k/2 => the rest will also have sum k/2


# A utility function that returns
# true if there is a subset of
# arr[] with sun equal to given sum
def isSubsetSum (arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # If last element is greater than sum, then
    # ignore it
    if arr[n-1] > sum:
        return isSubsetSum (arr, n-1, sum)

    ''' else, check if sum can be obtained by any of
    the following
    (a) including the last element
    (b) excluding the last element'''

    return isSubsetSum (arr, n-1, sum) or isSubsetSum (arr, n-1, sum-arr[n-1])

# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
def findPartion (arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % 2 != 0:
        return false

    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum (arr, n, sum // 2)


#if we want to do this with k sunbset,we need banktracking

bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for(int num:nums)sum+=num;
        if(k <= 0 || sum%k != 0)return false;
        vector<int> visited(nums.size(), 0);
        return canPartition(nums, visited, 0, k, 0, 0, sum/k);
    }

    bool canPartition(vector<int>& nums, vector<int>& visited, int start_index, int k, int cur_sum, int cur_num, int target){
        if(k==1)return true;
        if(cur_sum == target && cur_num >0 )return canPartition(nums, visited, 0, k-1, 0, 0, target);
        for(int i = start_index; i<nums.size(); i++){
            if(!visited[i]){
                visited[i] = 1;
                if(canPartition(nums, visited, i+1, k, cur_sum + nums[i], cur_num++, target))return true;
                visited[i] = 0;
            }
        }
        return false;
    }
