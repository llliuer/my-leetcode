func lengthOfLongestSubstring(s string) int {
    // s = "nfpdmpi"
    n := len(s)
    if n == 0 || n == 1{
        return n
    }

    var temp_str []string
    var res int
    // var *p int
    p := new(int)
    for i:=0; i<n; i++{
        if ! stringInSlice(string(s[i]), temp_str, p){ //如果s[i]不在temp_str内
            temp_str = append(temp_str , string(s[i])) 
        } else {
            temp_str = append(temp_str[*p+1:], string(s[i]))
        }
        if len(temp_str)>res{
            res = len(temp_str)
        }
        // fmt.Println(temp_str)
        // fmt.Println(len(temp_str))
        // fmt.Println(res)
        // fmt.Printf("\n")
    }
    return res
}

func stringInSlice(a string, s []string, p *int) bool {
    for i, b := range s{
        if a == b{
            *p = i
            return true
        }
    }
    return false
}
