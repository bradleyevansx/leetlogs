# LeetLogs

This repository serves as documentation for my progress in **leetcode** as well my general understanding of **data structures and algorithms**.

---

[![LeetCode Stats](https://leetcard.jacoblin.cool/SungJin-Woo?theme=light&font=Overpass%20Mono)](https://leetcode.com/SungJin-Woo)

---

Show some ❤️ by starring ⭐ this repository if you like it!

###### Contact for work, email: bradleyevans.x@gmail.com

![GitHub stars](https://img.shields.io/github/stars/bradleyevansx/leetlogs?style=social)
![GitHub forks](https://img.shields.io/github/forks/bradleyevansx/leetlogs?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/bradleyevansx/leetlogs?style=social)

[![linkedin](https://img.shields.io/badge/Support-Recommend%2FEndorse%20me%20on%20Linkedin-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/bradleymevans)

## Table of Contents 📖

- **[Repository Structure️](#repository-structure)**
- **[How To Use This Repository](#how-to-use-this-repository)**
- **[Repository Generation](#repository-generation)**

## Current Problem Set

### Blind 75 ![](https://img.shields.io/badge/Progress-5%2F75-0078D4)

The Blind 75 is a list of questions curated by an ex-meta engineer.

My goal in completing this set of questions is to force myself to finish a set of questions that includes all the important types of data structures and algorithms.

[Curated List of Top 75 LeetCode Questions](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)

| Problem                                                                                               | Difficulty                                                | Tags                                              | LeetCode                                                                                             |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [Two Sum](https://leetcode.com/problems/two-sum/)                                                     | <img src="https://img.shields.io/badge/-Easy-green" />    | `Arrays`, `Hash Table`                            | [✅](./003%20-%20Hash%20Maps/002%20-%20Two%20Sum/README.md)                                          |
| [Best Time to Buy and Sell a Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-a-stock/) | <img src="https://img.shields.io/badge/-Easy-green" />    | `Arrays`, `Dynamic Programming`, `Sliding Window` | [✅](./002%20-%20Two%20Pointers/001%20-%20Best%20Time%20to%20Buy%20and%20Sell%20a%20Stock/README.md) |
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)                               | <img src="https://img.shields.io/badge/-Easy-green" />    | `Arrays`, `Hash Table`                            | [✅](./003%20-%20Hash%20Maps/004%20-%20Contains%20Duplicate/README.md)                               |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)           | <img src="https://img.shields.io/badge/-Medium-orange" /> | `Arrays`, `Hash Table`                            | [✅](./001%20-%20Arrays%20and%20Strings/004%20-%20Product%20of%20Array%20Except%20Self/README.md)    |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                   | <img src="https://img.shields.io/badge/-Medium-orange" /> | `Arrays`, `Dynamic Programming`                   | [✅](./001%20-%20Arrays%20and%20Strings/005%20-%20Maximum%20Subarray/README.md)                      |
| [Three Sum](https://leetcode.com/problems/3sum/)                                                      | <img src="https://img.shields.io/badge/-Medium-orange" /> | `Arrays`, `Sorting`, `Two Pointers`               | [✅](./001%20-%20Arrays%20and%20Strings/006%20-%20Three%20Sum/README.md)                             |
| [Merge Invertvals](https://leetcode.com/problems/merge-intervals/)                                    | <img src="https://img.shields.io/badge/-Medium-orange" /> | `Arrays`, `Sorting`                               | [✅](./001%20-%20Arrays%20and%20Strings/007%20-%20Merge%20Intervals/README.md)                       |

## Repository Structure

Each topic has it's own directory and each problem a directory within it's topic.

Each topic will contain a **README** file with an introduction to the various topics as well as common techiniques for solving problems within said topic.

## How To Use This Repository

You can search for problems by topic.

Each topic will have an in depth explaination of the data structure or algorithm.

Feel free to open up a pull request and add to my explanations.

## Repository Generation

The entire repo is regenerated before pushing (eventually via github action).

All the data within the repository is held within the index.py file in the root directory.

You can generate all the files by running:

```zsh
python3 index.py
```

I did it this way so that I can change the formatting of all the README files in one place.
