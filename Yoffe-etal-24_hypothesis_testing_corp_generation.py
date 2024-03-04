def corp_generator(corp, intersection_set_mode = None, text_unit_length = 1, unk_token = None, delimiter = " ", verbose = True):
    """
    This function receives a desired pair of textual corpora (only those listed in Yoffe+24 Table 1) and a set of preprocessing specifications, and returns the processed text units and their associated real labels
    :param corp: Tuple/list of two strings, indicating the desired pair of corpora. e.g., ("Potter_1", "Lotr_2")
    :param intersection_set_mode: Vocabulary intersection mode. Has four options: (1) None: union of vocabularies of both texts. (2) "all": all features in the intersection of both texts. (3) "common_x": x most frequent features in the intersection of both vocabularies.
    (4) "average_3" x most frequent features in the WEIGHTED-AVERAGE intersection of both vocabularies (i.e., features whose weighted-average frequency across both corpora is the highest)
    :param text_unit_length: Integer indicating the number of words to be in each text unit
    :param unk_token: token to replace omitted words. Has two options: (1) None: omitted words are simply removed. (2) some string: omitted words are replaced by the input string
    :param verbose: if True, will print some useful info
    :return: list of processed text units, list of their associated real labels
    """

    def return_one_corp(this_corp):
        """
        This function receives a string representing of an abbreviated name of a corpus (see Yoffe+24 Table 1) and returns the unprocessed text
        :param this_corp: String of the desired text. e.g., "Potter_1"
        :return: Space-separated string of the text
        """
        if "spooky" in this_corp:

            df = pd.read_csv(main_path + "/Corpora_for_training/spooky_train.csv")

            author = this_corp.split("_")[1]

            df = df[df.loc[:, "author"] == author]

            text = " ".join([i.lower() for i in df['text'].to_numpy()])

            for p in string.punctuation:
                text = text.replace(p, "")

        if "Potter" in this_corp:

            this_book = this_corp.split("_")[1]

            # Read the text file
            with open(main_path + f"/Corpora_for_training/Potter/Potter_{this_book}.txt") as f:
                book = f.read().lower()
            f.close()

            book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            book = "\n".join([sent for sent in book.split("\n") if "j.k. rowling" not in sent])
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "") for sent in book]
                # book = book.replace(p, "")

            # text = " ".join([" ".join(sent.split()) for sent in book])
            #
            # if this_corp == "Potter_2":
            #
            #     # Read the text file
            #     with open(main_path + "/Corpora_for_training/Potter/Potter_2.txt") as f:
            #         book = f.read().lower()
            #     f.close()
            #
            #     book = re.sub('mr. ','mister ',book)
            #     book = re.sub('mrs. ','missus ',book)
            #     book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if "j.k. rowling" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if len(sent) > 5])
            #     book = re.sub('\n',' ',book)
            #     book = re.sub('  ',' ',book)
            #     book = book.split(". ")
            #
            #     for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #         book = [sent.replace(p, "") for sent in book]
            #
            # if this_corp == "Potter_3":
            #
            #     # Read the text file
            #     with open(main_path + "/Corpora_for_training/Potter/Potter_3.txt") as f:
            #         book = f.read().lower()
            #     f.close()
            #
            #     book = re.sub('mr. ','mister ',book)
            #     book = re.sub('mrs. ','missus ',book)
            #     book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if "j.k. rowling" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if len(sent) > 5])
            #     book = re.sub('\n',' ',book)
            #     book = re.sub('  ',' ',book)
            #     book = book.split(". ")
            #
            #     for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #         book = [sent.replace(p, "") for sent in book]
            #
            # if this_corp == "Potter_4":
            #
            #     # Read the text file
            #     with open(main_path + "/Corpora_for_training/Potter/Potter_4.txt") as f:
            #         book = f.read().lower()
            #     f.close()
            #
            #     book = re.sub('mr. ','mister ',book)
            #     book = re.sub('mrs. ','missus ',book)
            #     book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if "j.k. rowling" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if len(sent) > 5])
            #     book = re.sub('\n',' ',book)
            #     book = re.sub('  ',' ',book)
            #     book = book.split(". ")
            #
            #     for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #         book = [sent.replace(p, "") for sent in book]
            #
            # if this_corp == "Potter_5":
            #
            #     # Read the text file
            #     with open(main_path + "/Corpora_for_training/Potter/Potter_5.txt") as f:
            #         book = f.read().lower()
            #     f.close()
            #
            #     book = re.sub('mr. ','mister ',book)
            #     book = re.sub('mrs. ','missus ',book)
            #     book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if "j.k. rowling" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if len(sent) > 5])
            #     book = re.sub('\n',' ',book)
            #     book = re.sub('  ',' ',book)
            #     book = book.split(". ")
            #
            #     for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #         book = [sent.replace(p, "") for sent in book]
            #
            # if this_corp == "Potter_6":
            #
            #     # Read the text file
            #     with open(main_path + "/Corpora_for_training/Potter/Potter_6.txt") as f:
            #         book = f.read().lower()
            #     f.close()
            #
            #     book = re.sub('mr. ','mister ',book)
            #     book = re.sub('mrs. ','missus ',book)
            #     book = "\n".join([sent for sent in book.split("\n") if "page |" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if "j.k. rowling" not in sent])
            #     book = "\n".join([sent for sent in book.split("\n") if len(sent) > 5])
            #     book = re.sub('\n',' ',book)
            #     book = re.sub('  ',' ',book)
            #     book = book.split(". ")
            #
            #     for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #         book = [sent.replace(p, "") for sent in book]
            #
            # if this_corp == "Potter_7":
            #
            #     # Read the text file
            #     with open(main_path + "/Corpora_for_training/Potter/Potter_7.txt") as f:
            #         book = f.read().lower()
            #     f.close()
            #
            #     book = re.sub('mr. ','mister ',book)
            #     book = re.sub('mrs. ','missus ',book)
            #     book = "\n".join([sent for sent in book.split("\n") if "Chapter " not in sent])
            #     book = re.sub('\n',' ',book)
            #     book = re.sub('  ',' ',book)
            #     book = book.split(". ")
            #
            #     for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #         book = [sent.replace(p, "") for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Narnia" in this_corp:

            # Read the text file
            with open(main_path + "/Corpora_for_training/CS_Lewis/Narnia.txt") as f:
                book = f.read().lower()
            f.close()

            book = re.sub('mr. ','mister ',book)
            book = re.sub('mrs. ','missus ',book)
            book = re.sub('\n',' ',book)
            # book = re.sub('  ',' ',book)
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "") for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Percy" in this_corp:

            # Read the text file
            with open(main_path + "/Corpora_for_training/Percy/Percy_{}.txt".format(this_corp.split("_")[1])) as f:
                book = f.read().lower()
            f.close()

            book = " ".join([i for i in book.split("\n") if len(i) > 3])
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "").strip() for sent in book]

            text = re.sub(' +', ' ', " ".join([" ".join(sent.split()) for sent in book]))

        if "Lotr" in this_corp:

            import codecs
            f = codecs.open(main_path + "/Corpora_for_training/LotR/book_{}.txt".format(this_corp.split("_")[1]),"r", encoding = 'cp1252')
            text = f.read().lower()

            text = re.sub('\n',' ', text)
            text = re.sub('\r      ',' ', text)
            text = " ".join([contractions.fix(word) for word in text.split()])

            # percy = re.sub('  ',' ',percy)
            # text = text.split(". ")
            # for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
            #     text.replace(p, "")
            text = "".join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz -"]).split()
            text = " ".join([i for i in text if len(i) > 0])

        if "Silmarillion" in this_corp:

            import codecs
            f = codecs.open(main_path + "/Corpora_for_training/LotR/Silmarillion.txt", "r")
            text = f.read().lower()

            text = "\n".join([sent for sent in text.split("\n") if len(sent) > 5])
            text = re.sub('\n',' ', text)
            text = " ".join([contractions.fix(word) for word in text.split()])

            text = "".join([i for i in text if i in "abcdefghijklmnopqrstuvwxyz -"]).split()
            text = " ".join([i for i in text if len(i) > 0])

            # percy = re.sub('  ',' ',percy)
            # text = text.split(". ")
            # for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”", ";":
            #     text.replace(p, "")

        if "Screwtape" in this_corp:

            # Read the text file
            with open(main_path + "/Corpora_for_training/CS_Lewis/Screwtape.txt") as f:
                book = f.read().lower()
            f.close()

            book = re.sub('\n',' ', book)
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "").strip() for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Caspian" in this_corp:

            # Read the text file
            with open(main_path + "/Corpora_for_training/CS_Lewis/Caspian.txt") as f:
                book = f.read().lower()
            f.close()

            book = re.sub('\n',' ', book)
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "").strip() for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Dickens" in this_corp:

            this_book = this_corp.split("_")[1]

            # Read the text file
            with open(main_path + f"/Corpora_for_training/Dickens/{this_book}.txt") as f:
                book = f.read().lower()
            f.close()

            book = re.sub('\n',' ', book)
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "").strip() for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Holmes" in this_corp:

            this_book = this_corp.split("_")[1]

            # Read the text file
            with open(main_path + f"/Corpora_for_training/Doyle/Holmes_{this_book}.txt") as f:
                book = f.read().lower()
            f.close()

            book = re.sub('\n',' ', book)
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "").strip() for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Kipling" in this_corp:

            this_book = this_corp.split("_")[1]

            # Read the text file
            with open(main_path + f"/Corpora_for_training/Kipling/{this_book}.txt") as f:
                book = f.read().lower()
            f.close()

            book = re.sub('\n',' ', book)
            book = re.sub('--',' ', book)
            book = book.split(". ")
            book = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in book]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                book = [sent.replace(p, "").strip() for sent in book]

            text = " ".join([" ".join(sent.split()) for sent in book])

        if "Austen" in this_corp:

            this_corp = this_corp.split("_")[1]

            # Read the text file
            with open(main_path + f"/Corpora_for_training/Austen/{this_corp}.txt") as f:
                text = f.read().lower()
            f.close()

            text = text.split(". ")
            text = [" ".join([contractions.fix(word) for word in sent.split()]) for sent in text]

            for p in string.punctuation + "’" + "■" + "“" + "‘" + "•" + "—" + "”":
                text = [sent.replace(p, "").strip() for sent in text]

            text = " ".join([" ".join(sent.split()) for sent in text])

        return text

    def text_to_chunk(text_one_string, text_unit_length, delimiter = " "):

        """
        This function receives a string of separator-separated words, and divides it into chunks of length chunk_size (words)
        :param text_one_string: String of space-separated words (i.e., text)
        :param text_unit_length: Integer indicating number of words of each text unit
        :param delimiter: String indicating how to separate words. DEFAULT: space
        :return: List of strings of separator-separated words
        """

        text_by_words = text_one_string.split(delimiter)

        if len(text_by_words) > text_unit_length:
            text_by_chunks = [text_by_words[i:i + chunk_size] for i in range(0, len(text_by_words), text_unit_length)]
            text_by_chunks = [delimiter.join([word for word in sent if len(word) > 0]) for sent in text_by_chunks if len(sent) >= text_unit_length]
        else:
            text_by_chunks = text_by_words

        return text_by_chunks

    both_texts = [] # List that will contain both corpora

    for this_corp in corp: # Retreiving each corpus of the desired pair
        both_texts.append(return_one_corp(this_corp))

    text_1 = both_texts[0] # Space-separated string of the first text
    text_2 = both_texts[1] # Space-separated string of the second text

    if intersection_set_mode == "all":
        intersection_set = set(text_1.split()).intersection(set(text_2.split())) # Intersection of both texts

    if intersection_set_mode is not None and "common" in intersection_set_mode:
        nr_features = int(intersection_set_mode.split("_")[1]) # Number of desired most-frequent words in both texts
        intersection_set = set(text_1.split()).intersection(set(text_2.split())) # Intersection of both texts
        text_1_intersection = " ".join([word for word in text_1.split(" ") if word in intersection_set]) # Space-separated string of text 1 containing only the intersecting words
        text_2_intersection = " ".join([word for word in text_2.split(" ") if word in intersection_set]) # Space-separated string of text 2 containing only the intersecting words
        intersection_set = set([i[0] for i in Counter(text_1_intersection.split() + text_2_intersection.split()).most_common()[:nr_features]]) # Intersection set containing the nr_features most frequent words in both texts

    if intersection_set_mode is not None and "average" in intersection_set_mode: # Weighted-average most-frequent words

        nr_features = int(intersection_set_mode.split("_")[1]) # Number of desired most-frequent words in both texts
        intersection_set = set(text_1.split()).intersection(set(text_2.split())) # Common words
        text_1_intersection = " ".join([word for word in text_1.split(" ") if word in intersection_set]) # Space-separated string of text 1 containing only the intersecting words
        text_2_intersection = " ".join([word for word in text_2.split(" ") if word in intersection_set]) # Space-separated string of text 2 containing only the intersecting words

        word_count_1 = list(Counter(text_1_intersection.split())) # Counting words of text_1_intersection
        word_count_2 = list(Counter(text_2_intersection.split())) # Counting words of text_1_intersection

        all_words_1 = sum(list(word_count_1.values())) # Sum of all intersecting words in text 1
        all_words_2 = sum(list(word_count_2.values())) # Sum of all intersecting words in text 2

        intersection_words_avg = {word: (((word_count_1[word] / all_words_1) * (all_words_1 / (all_words_1 + all_words_2))) + ((word_count_2[word] / all_words_2) * (all_words_2 / (all_words_1 + all_words_2)))) for word in intersection_set} # Weighted average of the word frequency
        intersection_words_avg = dict(sorted(intersection_words_avg.items(), key = operator.itemgetter(1), reverse = True)) # Arranging by descending weighted-average word frequency
        words_sorted_avg_freq = list(intersection_words_avg.keys()) # List of words by descending order of their weighted-average
        intersection_set = sorted(set(words_sorted_avg_freq[:nr_features])) # Intersection set containing the x most-frequent weighted-average words

    if verbose:
        print(f"The desired intersection set of words (using the mode: {intersection_mode}) is of size: {len(intersection_set)}, and contains the following words:\n{sorted(intersection_set)}\n\n")

    if unk_token is not None: # Replacing words not in the intersection set with the desired token

        text_1 = re.sub(' +', ' ', " ".join([word if word in intersection_set else unk_token for word in text_1.split(" ")]).strip())
        text_2 = re.sub(' +', ' ', " ".join([word if word in intersection_set else unk_token for word in text_2.split(" ")]).strip())

    text_1 = text_to_chunk(text_1, chunk_size = text_unit_length) # text 1 arranged in text-units of the desired length
    text_2 = text_to_chunk(text_2, chunk_size = text_unit_length) # text 2 arranged in text-units of the desired length

    if verbose:
        print(f"Each text contains the following nr. of sentences (respectively): {len(text_1)}, {len(text_2)}")
        print(f"Average nr. of words per sentence: {round((np.average([len(i.split()) for i in text_1]) + np.average([len(i.split()) for i in text_2])) / 2., 1)}")

    texts_final = []
    for text_unit in text_1 + text_2:
        text_unit = re.sub(" ", delimiter, text_unit) # Using the desire delimiter to separate between words
        text_unit = " ".join([re.sub(r'[^a-zA-Z]', '', word) for word in text_unit.split()]) # Keeping only alphabetic characters in the text
        texts_final.append(text_unit)

    labels_textwise = np.array(([0] * len(text_1)) + ([1] * len(text_2)), dtype = int) # Assigning labels to the text units

    return np.array(texts_final, dtype = object), labels_textwise