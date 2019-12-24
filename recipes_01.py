from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [1, 1, 0, 0]
cls = tree.DecisionTreeClassifier()
cls = cls.fit(features, labels)
print(cls.predict([[160, 0]]))