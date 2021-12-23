int binary_search(int l, int r)
{
    int mid = (l + r) / 2;

    if (probe_check(l, mid))
        if (l == mid)
            return l;
        else
            return binary_search(l, mid);
    else
    if (r == mid + 1)
        return r;
    else
        return binary_search(mid + 1, r);
}

int main()
{
    int n = probe_init();

    probe_answer(binary_search(0, n));
}