#include <iostream>
#include <vector>

std::vector<int> isDoubled(std::vector<int> list){
    std::vector<int> toReturn;
    for (auto& a : list){
        for (auto& b : list){
            if((a == b * 2)){
                toReturn.emplace_back(b);
            }
        }
    }
    return toReturn;
}

int main(){

    std::vector<int> changed = {1,3,4,2,6,8};
    
    std::cout << "[";
    for (int num : isDoubled(changed)){
        std::cout << num << " ";
    }
    std::cout << "]";
    return 0;
}
