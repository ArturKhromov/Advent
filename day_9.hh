#ifndef DAY_9_HH
#define DAY_9_HH

#include <string>
#include <vector>


class DiskMap
{
public:
    DiskMap(const std::string &input);
    std::string get_disk_map();
    void calculate_block_representation();
    void optimize_block_representation();
    void optimize_block_representation_v2();
    uint64_t get_cheksum() const;
    std::string get_empty_space() const;
    std::string get_file_location() const;

private:
    std::vector<char> disck_map_;
    std::vector<int> block_representation_;
    size_t max_id_;
};

#endif // DAY_9_HH