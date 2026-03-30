class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // hash the numbers according to their count in an unordered map
        // add all of the pairs in the hash map into a priority queue with count being the first
        // element in the par.
        // iterate through the pq k times while getting its top and popping it.
        vector<int> outpt;
        unordered_map<int, int> mp;
        priority_queue<pair<int, int>> pq;
        for (int i = 0; i < nums.size(); i++){
            if (mp.find(nums[i]) == mp.end()){
                mp[nums[i]] = 1;
            }
            else{
                mp[nums[i]]++;
            }
        }
        for (auto it = mp.begin(); it != mp.end(); it++){
            pq.push({it->second, it->first});
        }
        for (int i = 0; i < k; i++){
            outpt.push_back(pq.top().second);
            pq.pop();
        }
        return outpt;
    }
};
