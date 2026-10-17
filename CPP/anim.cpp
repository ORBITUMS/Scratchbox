#include <iostream>
#include <thread>
#include <chrono>
#include <vector>

int main() {
  std::cout << "start" << std::endl;
  std::vector<char> chars = {'|', '/', '-', '\\'};
  int time = 200;
  while (true) 
  {
    for (char el : chars) {
        std::cout << "\r" << el << std::flush; // the flush pushes buffer in the console
        std::this_thread::sleep_for(std::chrono::milliseconds(time));
    }
  }

  return 0;
}