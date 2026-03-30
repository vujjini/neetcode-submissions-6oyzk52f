class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // add all of em into a hash map
        // traverse each one, check if its +1 exists in the map
        // if it does, keep on going until +1 doesnt exist
        // record the count as len_max
        // do the same for other numbers in the list which havent been visted before
        int max_len = 0;
        unordered_map<int, bool> mp;
        for (int i = 0; i < nums.size(); i++){
            mp[nums[i]] = false;
        }
        for (int i = 0; i < nums.size(); i++){
            if (mp[nums[i]] == true){
                continue;
            }
            int ct = 1;
            int next_num = nums[i]+1;
            if (mp.find(next_num) != mp.end()){
                ct++;
                mp[next_num] = true;
            }
            while(mp.find(next_num) != mp.end()){
                next_num++;
                if (mp.find(next_num) == mp.end()){
                    break;
                }
                else{
                    mp[next_num] = true;
                    ct++;
                }
            }
            max_len = max(ct, max_len);
            continue;
        }

        return max_len;

    }
};
