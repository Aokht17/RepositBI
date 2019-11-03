def vypryamitel(S):
    """
    function flats the given list
    :param S: list
    :return: flattened list
    """
    if S == []:
        return S
    if isinstance(S[0], list):
        return vypryamitel(S[0]) + vypryamitel(S[1:])
    return S[:1] + vypryamitel(S[1:])



