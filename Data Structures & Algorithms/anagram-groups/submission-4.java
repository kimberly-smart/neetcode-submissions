class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hash = new HashMap<>();

        for(String s: strs)
        {
            int[] key = new int[26];
            for(char c:s.toCharArray())
            {
                key[c -'a'] ++;
            }

            String k = Arrays.toString(key);
            hash.putIfAbsent(k, new ArrayList<>());
            hash.get(k).add(s);
        }

        return new ArrayList<>(hash.values());
    }
}

// 

