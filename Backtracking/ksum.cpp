#Problem 39 Given a set of candidate numbers (C) and a target number (T),
#find all unique combinations in C where the candidate numbers sums to T.
#The same repeated number may be chosen from C unlimited number of times.

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> combination;
        dfs(candidates, target, result, combination, 0);
        return result;
    }

    void dfs(vector<int>& nums, int target, vector<vector<int>>& result, vector<int>& combination, int begin) {
        if (!target) {
            result.push_back(combination);
            return;
        }
        for (int i = begin; i < nums.size() && target >= nums[i]; i++) {
            combination.push_back(nums[i]);
            dfs(nums, target - nums[i], result, combination, i);
            combination.pop_back();
        }
    }
};
