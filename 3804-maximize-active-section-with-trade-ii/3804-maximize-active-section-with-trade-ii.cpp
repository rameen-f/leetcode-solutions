typedef long long ll;

struct Node {
    int best = 0;
    array<int, 2> end{0};

    Node() {}
    Node(int x) {
        end[0] = end[1] = x;
    }
};

Node merge(Node &a, Node &b) {
    Node res;

    res.best = max(a.best, b.best);

    if (a.end[1] && b.end[0])
        res.best = max(res.best, a.end[1] + b.end[0]);

    res.end[0] = a.end[0] ? a.end[0] : b.end[0];
    res.end[1] = b.end[1] ? b.end[1] : a.end[1];

    return res;
}

struct SegTree {
    int n;
    vector<Node> st;

    void init(const vector<int> &a) {
        n = a.size();
        st.assign(4 * n + 5, Node());
        build(1, 0, n - 1, a);
    }

    Node build(int id, int l, int r, const vector<int> &a) {
        if (l == r)
            return st[id] = Node(a[l]);

        int mid = (l + r) / 2;

        Node left = build(id << 1, l, mid, a);
        Node right = build(id << 1 | 1, mid + 1, r, a);

        return st[id] = merge(left, right);
    }

    Node query(int id, int l, int r, int ql, int qr) {
        if (r < ql || l > qr)
            return Node();

        if (ql <= l && r <= qr)
            return st[id];

        int mid = (l + r) / 2;

        Node left = query(id << 1, l, mid, ql, qr);
        Node right = query(id << 1 | 1, mid + 1, r, ql, qr);

        return merge(left, right);
    }
};

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>> &queries) {

        int n = s.size();
        int ones = 0;

        vector<pair<int, int>> seg;
        vector<int> id(n);
        vector<int> zeroLen;

        for (int i = 0; i < n; i++) {
            if (s[i] == '1') ones++;

            if (i == 0 || s[i] != s[i - 1])
                seg.push_back({i, i});
            else
                seg.back().second = i;

            id[i] = seg.size() - 1;
        }

        for (auto &p : seg) {
            if (s[p.first] == '0')
                zeroLen.push_back(p.second - p.first + 1);
            else
                zeroLen.push_back(0);
        }

        SegTree st;
        st.init(zeroLen);

        vector<int> ans;

        for (auto &q : queries) {

            int l = q[0], r = q[1];

            int ls = id[l], rs = id[r];

            int leftLen = seg[ls].second - l + 1;
            int rightLen = r - seg[rs].first + 1;

            bool leftBorder = (l == 0 || s[l - 1] != s[l]);
            bool rightBorder = (r == n - 1 || s[r] != s[r + 1]);

            int L = leftBorder ? ls : ls + 1;
            int R = rightBorder ? rs : rs - 1;

            int best = 0;

            if (s[l] == '0' && !leftBorder) {
                int nxt = ls + 2;

                if (nxt < rs)
                    best = max(best, zeroLen[nxt] + leftLen);
                else if (nxt == rs)
                    best = max(best, leftLen + rightLen);
            }

            if (s[r] == '0' && !rightBorder) {
                int prv = rs - 2;

                if (prv > ls)
                    best = max(best, zeroLen[prv] + rightLen);
                else if (prv == ls)
                    best = max(best, leftLen + rightLen);
            }

            if (L <= R)
                best = max(best, st.query(1, 0, zeroLen.size() - 1, L, R).best);

            ans.push_back(ones + best);
        }

        return ans;
    }
};