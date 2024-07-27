#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

std::map<string,int> encode_or_decode;

vector<int> encode(){
    for(int i=0;i<256;++i){
        encode_or_decode[string(1,char(i))]=i;
        std::cout << encode_or_decode[string(1,char(i))] << endl;
    }
    std::ifstream in("precompress.txt");
    char c;
    std::string current_str;
    std::string next_str;
    std::vector<int> result;

    if(in.is_open()){
        while(in.get(c)){
            next_str=current_str + string(1,c);
            if(encode_or_decode.count(next_str)){
                current_str=next_str;
            }
            else{
                result.push_back(encode_or_decode[current_str]);
                encode_or_decode[next_str]=encode_or_decode.size();
                current_str=string(1,c);
            }
        }
        if(!current_str.empty()){
            result.push_back(encode_or_decode[current_str]);
        }
    }

    in.close();

    return result;
}

int main(){
    std::vector<int> encode_result=encode();
    ofstream out("aftercompress.txt");
    if(out.is_open()){
        out << encode_or_decode.size() << endl;
        for(auto values:encode_or_decode){
            out << values.first << " " << values.second << endl;
        }
        for(int code:encode_result){
            out << code << " ";
        }
    }

    out.close();

    return 0;
}