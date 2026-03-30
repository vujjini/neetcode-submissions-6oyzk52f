class Solution {
public:

    static bool compare(char a, char b){
        return a < b;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // init a hash map with key as sorted word and value as a list of strings
        // go thru all the words in the list
        // sort the word. NOTE: sort() func works for strings as well but qsort() doesn't.
        // it only works for arrays and the like
        // push the unsorted word to the value of the sorted word in the hash map
        vector<vector<string>> outpt;
        unordered_map<string, vector<string>> mp;
        for (int i = 0; i < strs.size(); i++){
            string s = strs[i];
            sort(s.begin(), s.end(), compare);
            mp[s].push_back(strs[i]);
        }
        for (auto it = mp.begin(); it != mp.end(); it++){
            outpt.push_back(it->second);
        }
        return outpt;
    }
};