# LabelMap

![python](https://img.shields.io/static/v1?logo=python&labelColor=3776AB&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Python3)
![pytorch](https://img.shields.io/static/v1?logo=pytorch&labelColor=EE4C2C&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Pytorch)
![tensorflow](https://img.shields.io/static/v1?logo=tensorflow&labelColor=FF6F00&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Tensorflow)
![keras](https://img.shields.io/static/v1?logo=keras&labelColor=D00000&color=ffffff&logoColor=ffffff&style=flat-square&label=%20&message=Keras)

***Generate label maps for ML/DL Projects***

## Usage

- With CSV file

    ```python
    from labelmap import LabelMap

    label_map = LabelMap(labels_csv="path-to-csv", labels_col_name="labels")   

    label_map.info() # print label map
    ```

- With CSV file and exclude some labels

    ```python
    from labelmap import LabelMap

    label_map = LabelMap(labels_csv="path-to-csv", labels_col_name="labels", exclude_labels=["cat", "dog"])    

    label_map.info() # print label map
    ```

- Without CSV file

    ```python
    from labelmap import LabelMap

    label_map = LabelMap()

    label_map.add("cat")
    label_map.add("dog")

    label_map.info() # print label map
    ```

## Parameters in `LabelMap` class

- `labels_csv` : `str`
  - The path to the csv file containing the labels and ids.
  - Not Required, default = `None`
- `labels_col_name` : `str`
  - The name of the column containing the labels.
  - Required if `labels_col_name` is set, default = `None`
- `ids_col_name` : `str`
  - The name of the column containing the ids.
  - Not Required, default = `None`
- `id_type` : `int/float`
  - The type of the ids.
  - Not Required, default = `int`
- `exclude_labels` : `list`
  - The labels to exclude from the label map.
  - Not Required, default = `None`

## Methods in `LabelMap` class

- `add(label)`
  - Add a label to the label map.
  - Args: `label -> str`
  - Return Type: `None`

- `force_get(label)`
  - Get the id of a label or if id not found then add the label and get.
  - Args: `label -> str`
  - Return Type: `None`

- `to_text(id)`
  - Get the label of an id.
  - Args: `id -> int/ float`
  - Return Type: `str`

- `to_id(label)`
  - Get the id of a label.
  - Args: `label -> str`
  - Return Type: `int/ float`

- `map()`
  - Get the label map as dict.
  - Args: `None`
  - Return Type: `dict`

- `labels()`
  - Get the list of labels.
  - Args: `None`
  - Return Type: `list`

- `info()`
  - Print the label map as table.
  - Args: `None`
  - Return Type: `None`

- `count()`
  - Get the number of labels.
  - Args: `None`
  - Return Type: `int`

- `as_dataframe()`
  - Label data dictionary to pandas dataframe.
  - Args: `None`
  - Return Type: `pandas.DataFrame`

- `save_csv(path)`
  - label data dictionary save to csv file.
  - Args: `path -> str`
  - Return Type: `None`
