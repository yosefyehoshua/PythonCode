#############################################################################
# FILE : ex10.py
# WRITER : Yosef Yehoshua, yosef12345, 302818513
# EXERCISE : intro2cs ex10 2015-2016
# DESCRIPTION : WikiNetwork articles system!
#############################################################################

#############################################################################
# CONSTANTS
#############################################################################
RANK_VALUE = 1
SUB_NUM = 1
RANK_GOT = 0


#############################################################################
# functions
#############################################################################


def read_article_links(file_name):
    """
    open a file and returns a list of tuples (article_name, neighbor_name)
    :param file_name: str
    :return: list of tuples (article_name, neighbor_name)
    """
    link_list = []
    file = open(file_name, 'r')
    file_name_to_srt = file.read()
    couples_list = file_name_to_srt.split('\n')
    for couple in couples_list:
        articles = couple.split('\t')
        tup = tuple(articles)
        if tup[0] != "":
            link_list.append(tup)
    return link_list


#############################################################################
# Article CLASS
#############################################################################
class Article:
    """
    A class representing of an Article
    """

    def __init__(self, name):
        """
        initialize Article class
        :param name: self.__name - article_name
        """
        self.__name = name
        self.__neighbors = set()
        self.__neighbors_name = set()
        self.__article_rank = RANK_VALUE

    def get_name(self):
        """
        :return: name of the article
        """
        return self.__name

    def add_neighbor(self, neighbor):
        """
        adds an obj "neighbor" to self.__neighbors - set().
        :param neighbor: obj
        """
        self.__neighbors.add(neighbor)

    def get_neighbors(self):
        """
        :return: a set with all of article neighbors.
        """
        return list(self.__neighbors)

    def get_neighbors_name(self):
        """
        :return: set of all neighbors names.
        """
        for neighbor in self.__neighbors:
            self.__neighbors_name.add(neighbor.get_name())
        return self.__neighbors_name

    def get_article_rank(self):
        """
        :return: the article rank
        """
        return self.__article_rank

    def update_article_rank(self, new_rank):
        """
        updates a new rank for an article
        :param new_rank: just a number
        :return self.__article_rank - the new rank
        """
        self.__article_rank = new_rank
        return self.__article_rank

    def __repr__(self):
        """
        :return: str of the article an a list of its neighbors
        """
        for neighbor in self.__neighbors:
            self.__neighbors_name.add(neighbor.get_name())
        article_srt = (self.__name, list(self.__neighbors_name))
        return str(article_srt)

    def __len__(self):
        """
        :return: len of self.__neighbors
        """
        return len(self.__neighbors)

    def __contains__(self, article):
        """
        check if article is in self.__neighbors & return a boolean value
        :param article: obj
        :return: True/False
        """
        return article in self.__neighbors


#############################################################################
# WikiNetwork CLASS
#############################################################################
class WikiNetwork:
    def __init__(self, link_list=[]):
        """
        initilaze class WikiNetwork
        :param link_list: list of tuples
        """
        self.__network = dict()
        self.update_network(link_list)
        self.__link_list = link_list
        self.__article_list = []
        self.__title_list = []

    def update_network(self, link_list):
        """
        gets a list of couples (tuples) of articles & update self.__network
        :param link_list: list of couples (tuples) of articles
        """
        for couple in link_list:
            if couple[0] not in self.__network:
                self.__network[couple[0]] = Article(couple[0])
            if couple[1] not in Article(couple[0]).get_neighbors():
                self.__network[couple[0]].add_neighbor(Article(couple[1]))
            if couple[1] not in self.__network:
                self.__network[couple[1]] = Article(couple[1])

    def get_articles(self):
        """
        :return: all of the Articles (items) in self.__network
        """
        for article_name in self.__network:
            self.__article_list.append(self.__network[article_name])
        return self.__article_list

    def get_titles(self):
        """
        :return: all of the Articles (keys) names in self.__network
        """
        for article_name in self.__network:
            self.__title_list.append(article_name)
        return sorted(self.__title_list)

    def __contains__(self, article_name):
        """
        check if article is in self.__neighbors & return a boolean value
        :param article_name: article_name
        :return: True/False
        """
        return article_name in self.get_titles()

    def __len__(self):
        """
        :return: number of Articles in self.__network
        """
        return len(self.__network)

    def __repr__(self):
        """
        :return: if a given Article is in self.__network
        """
        return str(self.__network)

    def __getitem__(self, article_name):
        """
        :param article_name: article_name
        :return: returns an Article obj of a given article name
        """
        if article_name in self.__network:
            return self.__network[article_name]
        else:
            raise KeyError(article_name)

    def page_rank(self, iters, d=0.9):
        """
        utilize PageRank algorithm (for more info. visit:
        https://en.wikipedia.org/wiki/PageRank#Damping_factor)
        :param iters: number of iterations (int)
        :param d: damping factor (number between 0 to 1)
        :return: a list of sorted article
        """
        ranked_list = []
        one_minus_d = SUB_NUM - d
        counter = 0
        articles_rank = dict()
        if iters == 0:
            return self.get_titles()
        while counter < iters:
            counter += 1
            articles_rank = {
                article: [self[article].get_article_rank(), RANK_GOT] for
                article
                in self.get_titles()}
            for article in self.__network.values():
                art_obj = article
                art_neig = article.get_neighbors()
                give_away = (art_obj.get_article_rank() * d) / len(art_neig)
                new_rank = art_obj.update_article_rank(
                    art_obj.get_article_rank() -
                    art_obj.get_article_rank() * d)
                articles_rank[art_obj.get_name()][0] = new_rank
                for neighbor in art_neig:
                    neighbor = neighbor.get_name()
                    articles_rank[neighbor][1] += give_away
            for article in articles_rank:
                articles_rank[article][0] = articles_rank[article][
                                                1] + one_minus_d
                self.__getitem__(article).update_article_rank(
                    articles_rank[article][0])
        for article in articles_rank:
            rank = article, articles_rank[article][0]
            ranked_list.append(rank)
        ranked_list2 = sorted(ranked_list, key=lambda x: (-x[1], x[0]))
        return [tup[0] for tup in ranked_list2]

    def jaccard_index(self, article_name):
        """
        gets an article_name and returns a list of an ordered (big to small)
        articles by jaccard indexes of all the articles given
        :param article_name: str - article_name
        :return: list of an ordered articles by  jaccard indexes of all the
        given
        """
        if not self.__contains__(article_name) or len(
                self[article_name].get_neighbors()) == 0:
            return
        jaccard_index = dict()
        article_neighbors = {neighbor.get_name() for neighbor in
                             self[article_name].get_neighbors()}
        for article in self.__network.values():
            art_neig = set(neighbor.get_name() for neighbor in
                           self[article.get_name()].get_neighbors())
            union = art_neig.union(article_neighbors)
            inter = art_neig.intersection(article_neighbors)
            if len(union) != 0:
                jaccard_index[article.get_name()] = len(inter) / len(union)
            else:
                return

        indexed_list = sorted(jaccard_index.items(), key=lambda x: x[0])
        indexed_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)
        return [art[0] for art in indexed_list]

    def popularity_calculator(self, article_name):
        """
        calculate the numbers of articles that address article_name
        :param article_name: str - a given article
        :return: int - numbers of articles that address article_name
        """
        popularity_num = 0
        for article in self.__network:
            pointed = self[article].get_neighbors_name()
            if article_name in pointed:
                popularity_num += 1
        return popularity_num

    def popularity_finder(self, article_name):
        """
        gets an article_name and returns the neighbor with the highest
        popularity number (also by name).
        :param article_name: str - article_name
        :return: str -  suited neighbor for path
        """
        popularity_dic = dict()
        for neighbor in self[article_name].get_neighbors_name():
            popularity_num = self.popularity_calculator(neighbor)
            popularity_dic[neighbor] = popularity_num
        popularity_list = sorted(popularity_dic.items(),
                                 key=lambda x: (-x[1], x[0]))
        return popularity_list[0][0]

    def path_generator(self, article_name):
        """
        generate the next path (article) to go to
        :param article_name: str
        :return: cur - next article in path
        """
        cur = article_name
        yield cur
        while len(self[cur]) != 0:
            cur = self.popularity_finder(cur)
            yield cur
        raise StopIteration

    def travel_path_iterator(self, article_name):
        """
        gets an article_name and return an iterator- the article most popular
        neighbor.
        :param article_name: str
        :return: iterator - article name (next in path)
        """
        if len(self) == 0:
            return iter([])
        next = iter(self.path_generator(article_name))
        return next

    def neighbors_union(self, article_set):
        """
        gets a set of articles and returns a set with all their neighbors
        :param article_set: set of articles
        :return: set of neighbors
        """
        neighbors_set = set()
        set_list = [article_set]
        for article in article_set:
            set_list.append(self[article].get_neighbors_name())
        art_set = neighbors_set.union(*set_list)
        return art_set

    def friends_by_depth(self, article_name, depth):
        """
        gets a number (depth) an article (article_name) and returns a list of
        all the neighbors that linked to article in depth steps or less.
        :param article_name: str
        :param depth: int - number of depth
        :return: list of neighbor in depth
        """
        if article_name in self.__network:
            counter = 0
            article_set = set()
            article_set.add(article_name)
            while counter < depth:
                counter += 1
                article_set = self.neighbors_union(article_set)
            return list(article_set)
        else:
            return None
