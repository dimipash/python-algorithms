def transform_data(
    df: pd.DataFrame, numeric_cols: list[str] = None, categorical_cols: list[str] = None
) -> pd.DataFrame:
    """
    Applies common data transformations to a pandas DataFrame.

    Time Complexity: O(n*m) where n is number of rows and m is number of columns
    Space Complexity: O(n*k) where k is number of unique categorical values

    Args:
        df: Input DataFrame
        numeric_cols: List of numeric column names to normalize
        categorical_cols: List of categorical column names to encode

    Returns:
        Transformed DataFrame

    Example:
        >>> data = {
        ...     'age': [25, 30, 35],
        ...     'income': [50000, 60000, 70000],
        ...     'city': ['NYC', 'LA', 'CHI']
        ... }
        >>> df = pd.DataFrame(data)
        >>> transform_data(df,
        ...               numeric_cols=['age', 'income'],
        ...               categorical_cols=['city'])
    """
    df_transformed = df.copy()

    # Normalize numeric columns
    if numeric_cols:
        scaler = MinMaxScaler()
        df_transformed[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Encode categorical columns
    if categorical_cols:
        df_transformed = pd.get_dummies(
            df_transformed, columns=categorical_cols, drop_first=True
        )

    return df_transformed


def transform_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies multiple feature engineering transformations.

    Args:
        df: Input DataFrame

    Returns:
        DataFrame with engineered features
    """
    df_features = df.copy()

    # Log transform skewed numeric columns
    numeric_cols = df_features.select_dtypes("number").columns
    skewed_cols = numeric_cols[df_features[numeric_cols].skew().abs() > 1]
    df_features[skewed_cols] = np.log1p(df_features[skewed_cols])

    # Bin continuous variables
    df_features["age_group"] = pd.qcut(
        df_features["age"], q=5, labels=["Q1", "Q2", "Q3", "Q4", "Q5"]
    )

    # Create interaction features
    df_features["income_per_age"] = df_features["income"] / df_features["age"]

    return df_features
