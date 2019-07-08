import Data.Char
import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> (Int, Int)
readInput s = (l, h)
    where 
        li = (map read) $ words s
        l = head li
        h = last li

writeOutput :: Int -> String
writeOutput = show

solve :: (Int, Int) -> Int
solve (l,h)
    | l > h = 0
    | otherwise = (count l) + solve (l + 1, h)
    
count :: Int -> Int
count n = if uniqueTest ds && divisTest ds n then 1 else 0
    where 
        ds = digits n

digits :: Int -> [Int]
digits s = sort [(ord d - ord '0') | d <- (show s)]

uniqueTest :: [Int] -> Bool
uniqueTest (d:[]) = True
uniqueTest (c:d:ds)
    | c == d = False
    | otherwise = uniqueTest (d:ds)

divisTest :: [Int] -> Int -> Bool
divisTest (d:[]) n = n `mod` d == 0
divisTest (d:ds) n = d /= 0 && n `mod` d == 0 && divisTest ds n