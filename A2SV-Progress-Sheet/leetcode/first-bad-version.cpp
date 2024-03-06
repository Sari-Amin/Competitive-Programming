// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int bad;
        int l = 0, r = n, mid;
        while (l <= r)
        {
            mid = (l + r) / 2;
            // cout << mid << l<< r<<endl;
            if (isBadVersion(mid) && !isBadVersion(mid - 1)) 
            {
                bad = mid;
                break;
            }
            else
            {
                r = mid - 1;
            }
        }
        return bad;
    }
};