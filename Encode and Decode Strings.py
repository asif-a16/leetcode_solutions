class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for str in strs:
            final_str += str
            final_str += "🎄"
        return final_str

    def decode(self, s: str) -> List[str]:
        strs2 = s.split("🎄")
        
        return strs2[:-1]
