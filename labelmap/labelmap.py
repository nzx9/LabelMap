import pandas as pd
import os


class LabelMap:
    """
    LabelMap
    This class is a map between labels and ids.
    Parameters
    ----------
    labels_csv : str
        The path to the csv file containing the labels and ids.
    labels_col_name : str
        The name of the column containing the labels.
    ids_col_name : str
        The name of the column containing the ids.
    id_type : type
        The type of the ids.
    exclude_labels : list
        The labels to exclude from the label map.

    Attributes
    ----------
    label_map : dict
        The map between labels and ids.
    label_map_inv : dict
        The map between ids and labels.
    label_count : int
        The number of labels.
    label_data : pandas.DataFrame
        The dataframe containing the labels and ids.

    Methods
    -------
    add(label)
        Add a label to the label map.
    force_get(label)
        Get the id of a label or if id not found then add the label and get.
    to_text(id)
        Get the label of an id.
    to_id(label)
        Get the id of a label.
    map()
        Get the label map as dict.
    labels()
        Get the list of labels.
    info()
        Print the label map as table.
    count()
        Get the number of labels.
    as_dataframe()
        Label data dictionary to pandas dataframe.
    save_csv(path)
        label data dictionary save to csv file.
    """

    __label_map__ = {}
    __label_map_inv__ = None
    __label_count__ = 0
    __label_data__ = None
    __cache_outdated__ = False
    __type__ = int

    def __init__(
        self,
        labels_csv=None,
        labels_col_name=None,
        ids_col_name=None,
        id_type=int,
        exclude_labels: list = None,
    ):
        if labels_csv != None:
            if id_type != float and id_type != int:
                raise ValueError("id_type must be a int or float type")
            self.__type__ = id_type
            self.__label_data__ = pd.read_csv(labels_csv)
            self.__from_csv__(self.__label_data__, labels_col_name, ids_col_name)
        if type(exclude_labels) != list and exclude_labels != None:
            raise ValueError("exclude_labels must be a list")
        else:
            self.exclude_labels = exclude_labels

    def __from_csv__(self, label_data, labels_col_name, ids_col_name):
        self.__cache_outdated__ = True
        if labels_col_name == None:
            raise ValueError("lable_col_name can't be None if labels_csv is not None")
        for i in range(0, len(label_data)):
            row = label_data.iloc[i]
            if self.__label_map__.get(row[labels_col_name]) == None:
                _id = self.__type__(self.__label_count__)
                if ids_col_name != None:
                    _id = row[ids_col_name]
                if (
                    self.exclude_labels == None
                    or row[labels_col_name] not in self.exclude_labels
                ):
                    self.__label_map__[row[labels_col_name]] = _id
                    self.__label_count__ += 1

    def add(self, label):
        """
        Add a label to the label map.
        Args
        ----------
        label -> string
        """
        if (
            self.exclude_labels == None or label not in self.exclude_labels
        ) and self.__label_map__.get(label) == None:
            self.__label_map__[label] = self.__type__(self.__label_count__)
            self.__cache_outdated__ = True
            self.__label_count__ += 1

    def remove(self, label):
        """
        Remove a label from the label map.
        Args
        ----------
        label -> string
        """
        if self.__label_map__.get(label) != None:
            del self.__label_map__[label]
            self.__label_count__ -= 1
            self.__cache_outdated__ = True

    def force_get(self, label) -> int:
        """
        Get the id of the given label, if id of the label is None then add the label and return id.
        Args
        ----------
        label -> string
        """

        if self.__label_map__.get(label) == None:
            self.add(label)
        return self.__label_map__.get(label)

    def to_text(self, id) -> str:
        """
        Get the label of an id.
        Args
        ----------
        id -> int/ float
        """
        if self.__label_map_inv__ == None or self.__cache_outdated__:
            self.__label_map_inv__ = {v: k for k, v in self.__label_map__.items()}
            self.__cache_outdated__ = False
        return self.__label_map_inv__[id]

    def to_id(self, label) -> int:
        """
        Get the id of the given label.
        Args
        ----------
        label -> string
        """
        return self.__label_map__[label]

    def map(self) -> dict:
        """
        Get the label map as dict.
        Args
        ----------
        None
        """
        return self.__label_map__

    def labels(self) -> list:
        """
        Get the list of lables
        Args
        ----------
        None
        """
        lst = []
        for label in self.__label_map__:
            lst.append(label)
        return lst

    def info(self) -> None:
        """
        Print the label map as table
        Args
        ----------
        None
        """
        print("Label Map\n")
        print("{:>7} | {:<50}".format("ID", "LABEL"))
        print(
            "{:>7}+{:<50}".format(
                "--------", "----------------------------------------------"
            )
        )
        for label in self.__label_map__:
            print("{:>7} | {:<50}".format(self.to_id(label), label))

        print("\nTotal Label Count: {}".format(self.__label_count__))

    def count(self) -> int:
        """
        Get the number of labels.
        Args
        ----------
        None
        """
        return len(self.__label_map__)

    def as_dataframe(self) -> pd.DataFrame:
        """
        Label data dictionary to pandas dataframe.
        Args
        ----------
        None
        """
        return pd.DataFrame.from_dict(self.__label_data__)

    def save_csv(self, path: str, overwrite: bool = False) -> None:
        """
        label data dictionary save to csv file.
        Args
        ----------
        path -> str
        """
        if path[-4:] != ".csv":
            path = path + ".csv"
        if os.path.isfile(path) and not overwrite:
            raise FileExistsError("File already exists in {}".format(path))
        else:
            with open(path, "w") as f:
                f.write(
                    "id,label\n"
                    + "\n".join(
                        [
                            "{},{}".format(self.to_id(label), label)
                            for label in self.__label_map__
                        ]
                    )
                )
