    import pickle


load_model = pickle.load(open('dib_79.pkl', 'rb'))

pred = load_model.predict([[10, 20, 30, 40, 50, 60,70, 80]])

if pred[0] == 0:
    print('Person is dibetic')
else:
    print('Person is not dibetic')