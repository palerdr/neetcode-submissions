class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        char [] schars = s.toLowerCase().toCharArray();
        char [] tchars = t.toLowerCase().toCharArray();
        Arrays.sort(schars);
        Arrays.sort(tchars);
        return Arrays.equals(schars,tchars);
    }
}
