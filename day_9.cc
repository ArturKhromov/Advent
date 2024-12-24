#include "day_9.hh"
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>

DiskMap::DiskMap(const std::string &input)
{
    disck_map_ = std::vector<char>();
    for (const char &c : input)
    {
        disck_map_.push_back(c);
    }
}

std::string DiskMap::get_disk_map()
{
    std::ostringstream oss;
    for (const uint64_t &f : block_representation_)
    {
        if (f == -1)
        {
            oss << '.';
        }
        else
        {
            oss << f;
        }
    }
    return oss.str();
}

void DiskMap::calculate_block_representation()
{
    uint64_t idx = 0;
    block_representation_ = std::vector<int>();
    auto it_original = disck_map_.begin();
    while (it_original != disck_map_.end())
    {
        const uint64_t file_length = static_cast<uint64_t>(*it_original) - '0';
        for (uint64_t i = 0; i < file_length; i++)
        {
            block_representation_.push_back(idx);
        }
        it_original++;
        if (it_original == disck_map_.end())
        {
            break;
        }
        const uint64_t empty_space = static_cast<uint64_t>(*it_original) - '0';
        for (uint64_t i = 0; i < empty_space; i++)
        {
            block_representation_.push_back(-1);
        }
        it_original++;
        idx++;
    }
    max_id_ = idx;
}

void DiskMap::optimize_block_representation()
{
    for (size_t i = 0, j = block_representation_.size() - 1; i < j; j--)
    {
        while (block_representation_[j] == -1 && j > i)
        {
            j--;
        }
        while (block_representation_[i] != -1 && i < j)
        {
            i++;
        }
        std::swap(block_representation_[i], block_representation_[j]);
    }
}

void DiskMap::optimize_block_representation_v2()
{
    for (size_t j = block_representation_.size() - 1; j > 0; j--)
    {
        while (block_representation_[j] == -1 && j > 0)
        {
            j--;
        }
        const size_t end = j;
        const size_t id = block_representation_[j];
        size_t length_r = 0;
        while (block_representation_[j] == id && j > 0)
        {
            j--;
            length_r++;
        }
        j++;

        for (size_t i = 0; i < j; i++)
        {
            while (block_representation_[i] != -1 && i < j)
            {
                i++;
            }
            const size_t start_l = i;
            size_t length_l = 0;
            while (block_representation_[i] == -1 && i < j)
            {
                i++;
                length_l++;
            }
            i--;

            if (length_l >= length_r)
            {
                std::swap_ranges(block_representation_.begin() + start_l,
                                 block_representation_.begin() + start_l + length_r, block_representation_.begin() + end - length_r + 1);
                break;
            }
        }
    }
}

uint64_t DiskMap::get_cheksum() const
{
    uint64_t checksum = 0;
    for (size_t i = 0; i < block_representation_.size(); i++)
    {
        if (block_representation_[i] != -1)
        {
            checksum += i * block_representation_[i];
        }
    }
    return checksum;
}

std::string DiskMap::get_empty_space() const
{
    std::ostringstream oss;

    for (int i = 0; i < block_representation_.size(); i++)
    {
        if (block_representation_[i] == -1)
        {
            const size_t start = i;
            oss << "Empty block: ";
            while (block_representation_[i] == -1 && i < block_representation_.size())
            {
                i++;
            }
            oss << "Start: " << start << " End: " << i - 1 << std::endl;
        }
    }
    return oss.str();
}

std::string DiskMap::get_file_location() const
{

    std::map<int, std::pair<size_t, size_t>> locations;

    for (int i = 0; i < block_representation_.size(); i++)
    {
        if (block_representation_[i] != -1)
        {
            const size_t start = i;
            const int id = block_representation_[i];
            while (block_representation_[i] == id && i < block_representation_.size())
            {
                i++;
            }
            i--;
            locations[id] = std::make_pair(start, i);
        }
    }
    std::ostringstream oss;
    for (const auto &l : locations)
    {
        oss << "File " << l.first << ": " << l.second.first << " - " << l.second.second << std::endl;
    }
    return oss.str();
}

int main()
{
    const std::string test_input = "2333133121414131402";
    std::ifstream file("./input/input_9.txt");
    std::string line;
    std::getline(file, line);

    DiskMap disk_map(line);

    disk_map.calculate_block_representation();
    // std::cout << disk_map.get_disk_map() << std::endl;
    //  disk_map.optimize_block_representation();
    disk_map.optimize_block_representation_v2();
    // std::cout << disk_map.get_disk_map() << std::endl;
    std::cout << "Checksum: " << disk_map.get_cheksum() << std::endl;
    std::ofstream output_file("./output/empty_space.txt");
    output_file << disk_map.get_empty_space();
    output_file << disk_map.get_file_location();
    output_file.close();

    return 0;
}
