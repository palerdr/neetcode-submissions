use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut store: HashMap<[u8; 26], Vec<String>> = HashMap::new();
        for s in strs {
            let mut raw_key = [0u8; 26];
            for b in s.bytes() {
                raw_key[(b - b'a') as usize] += 1;
                }
            store.entry(raw_key).or_insert(Vec::new()).push(s);
            }
        store.into_values().collect()
    }
}
