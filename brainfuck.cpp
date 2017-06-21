#include <iostream>
#include <map>

using RESB = std::string;

int main() {
    uint64_t ip = 0; RESB mem(512,'0'), in("+>.");
    std::map<char, void(*)(uint64_t&, RESB&, RESB&)> inst {
        {'>', [](uint64_t& i, RESB& m, RESB& s){++i;}},
        {'<', [](uint64_t& i, RESB& m, RESB& s){--i;}},
        {'+', [](uint64_t& i, RESB& m, RESB& s){m[i] += 1;}},
        {'-', [](uint64_t& i, RESB& m, RESB& s){m[i] -= 1;}},
        {'.', [](uint64_t& i, RESB& m, RESB& s){putchar(m[i]);}},
        {'[', [](uint64_t& i, RESB& m, RESB& s){if(m[i] == '\0') for(;s[i] != ']' ;i+=1);}},
        {']', [](uint64_t& i, RESB& m, RESB& s){if(m[i] != '\0') for(;s[i] != '[' ;i-=1);}},
        {',', [](uint64_t& i, RESB& m, RESB& s){m[i] = getchar();}},
    };

    while(ip < in.size()) {
        inst[in[ip]](ip, mem, in);
        ++ip;
    }
}
