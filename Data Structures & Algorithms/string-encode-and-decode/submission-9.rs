impl Solution {
    // Encodes a list of strings to a single string.
    pub fn encode(strs: Vec<String>) -> String {
        let mut result = String::new();
        for s in strs {
            // Push "length" + "!" + "content"
            result.push_str(&format!("{}!{}", s.len(), s));
        }
        result
    }

    // Decodes a single string back into a list of strings.
    pub fn decode(s: String) -> Vec<String> {
        let mut result = Vec::new();
        let bytes = s.as_bytes(); // Work with raw bytes for performance
        let mut i = 0;
        
        while i < bytes.len() {
            // 1. Find the '!' delimiter
            let mut j = i;
            while bytes[j] != b'!' {
                j += 1;
            }
            
            // 2. Parse the length from the slice
            let length: usize = std::str::from_utf8(&bytes[i..j])
                .unwrap()
                .parse()
                .unwrap();
            
            // 3. Extract the string content
            i = j + 1; // Move past the '!'
            let content = std::str::from_utf8(&bytes[i..i + length]).unwrap();
            result.push(content.to_string());
            
            // 4. Advance pointer
            i += length;
        }
        result
    }
}