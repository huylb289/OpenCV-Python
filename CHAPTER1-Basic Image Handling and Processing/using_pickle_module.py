import pickle

# save mean and principal components
f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean, f)
pickle.dump(V,f)

f.close()

# load mean and principal components
f = open('font_pca_modes.pkl', 'rb')
# load in order of save
immean = pickle.load(f)
V = pickle.load(f)
f.close()


# Alternative method
# save array to file
savetxt('test.txt', x, '%i')
x = loadtxt('test.txt')
