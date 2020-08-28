import numpy as np

#%% 
def sudoku_solver(sudoku):
    K = int(np.sqrt(len(sudoku)))
    sudoku_flat = sudoku.flatten()
    sudoku_set = np.vectorize(lambda x: {x})(sudoku)
    
    
    #%% square indices
    # col_indices = np.tile(np.arange(K**2), [K**2,1])
    # row_indices = col_indices.T
    square_indices = np.kron(np.arange(K**2).reshape(K,K), 
                             np.ones([K,K]))
    
    # # vectorise row, col, square indices (row-wise)
    # col_indices_flat = col_indices.flatten()
    # row_indices_flat = row_indices.flatten()
    # square_indices_flat = square_indices.flatten()
    
    
    #%% indices on sudoku grid
    
    # sequence index row-wise
    sudoku_indices_flat = np.arange(K**2**2)
    sudoku_indices = sudoku_indices_flat.reshape(K**2,K**2)
    
    
    #%% combined vectorised indices by row, col, square
    vec_sudoku_indices = \
        [sudoku_indices[i,:] for i in range(K**2)] + \
        [sudoku_indices[:,j] for j in range(K**2)] + \
        [sudoku_indices[square_indices==k] for k in range(K**2)]
    vec_sudoku_indices_arr = np.array(vec_sudoku_indices)
    
    
    #%% 
    # element showing possible combinations
    X = np.repeat(set(range(1,K**2+1)), K**2**2).reshape(K**2,K**2)
    X[sudoku!=0] = sudoku_set[sudoku!=0]
    X_flat = X.flatten()   # vectorised version
    
    # which elements are non-zero (by vectorised indices)
    new_solved_indices = np.where(sudoku_flat!=0)[0]
    solved_indices = new_solved_indices
    
    # initialise tree variables
    X_flat_tree = np.array([X_flat])
    new_solved_indices_tree = np.array([new_solved_indices])

    
    #%% reduction 
    def reduce_sudoku(X_flat, vec_indices, z):
        # remove z from array of sets
        for i in vec_indices:
            X_flat[i] = X_flat[i] - z #setdiff(X_flat[i], z)

    
    #%% reduction function
    def reduction_cycle(X_flat, new_solved_indices):
        # m = 0
        # solved_indices = np.where(sudoku_flat!=0)[0]
        solved_indices = np.where(np.vectorize(len)(X_flat)==1)[0]
        while len(new_solved_indices)>0:
            # m += 1
            #%% Reduction
            
            # Reduction-step: Reduce X-flat by rows, cols, squares
            for k in new_solved_indices:
                z = X_flat[k]
                
                # which vector indices contain k?
                vec_index_with_k_bool = [(k in sudoku_index) for sudoku_index in vec_sudoku_indices]
                vec_indices = np.unique(vec_sudoku_indices_arr[vec_index_with_k_bool,:])
                vec_indices_without_k = vec_indices[vec_indices!=k]
                                
                reduce_sudoku(X_flat, vec_indices_without_k, z)
                    
            #%% Identify solved cells
            
            # Identify solved indicies
            nonsolved_indices = set(sudoku_indices_flat) - set(solved_indices)
            new_solved_indices = [k for k in list(nonsolved_indices) if len(X_flat[k])==1]
            solved_indices = np.concatenate((solved_indices, new_solved_indices))
            
        return X_flat, solved_indices

    # def masked_argmin(a, limit):
    #     valid_idx = np.where(a>=limit)[0]
    #     return valid_idx[a[valid_idx].argmin()]

    #%% start solving sudoku
    M = K**2**2
    for m in range(M):
        solved_indices_tree = []
        is_possible_sudoku_tree = []
        for i in range(len(X_flat_tree)):
            X_flat = X_flat_tree[i]
            new_solved_indices = new_solved_indices_tree[i]
            X_flat_reduce, solved_indices = reduction_cycle(X_flat, new_solved_indices)
            
            is_possible_sudoku_tree.append(np.all(np.vectorize(len)(X_flat_reduce) > 0))
            X_flat_tree[i] = X_flat_reduce
            solved_indices_tree.append(solved_indices)
        
        # X_flat_tree = X_flat_tree[np.where(is_possible_sudoku_tree)]
        X_flat_tree = X_flat_tree[np.array(is_possible_sudoku_tree)]
        solved_indices_tree = [solved_indices_tree[j] for j in range(len(solved_indices_tree)) if is_possible_sudoku_tree[j]]
        
        # see if it's solved
        solved_indices_tree_len = np.array([len(x) for x in solved_indices_tree])
        # solved_indices_tree_len = np.vectorize(len)(solved_indices_tree)
        # solved_indices_tree_len = np.apply_along_axis(len, 1, solved_indices_tree)
        if np.any(solved_indices_tree_len == K**2**2):
            # print("Sudoku solved!")
            X_flat = X_flat_tree[solved_indices_tree_len == K**2**2]
            X_flat = X_flat[0]
            sudoku_solved = np.array([next(iter(v)) for v in X_flat]).reshape(K**2, K**2)
            return(sudoku_solved)
        
        
        #%% guess
        
        # newtree variables
        X_flat_newtree = np.empty((1,K**2**2), dtype=int)
        new_solved_indices_newtree = np.empty((1,1), dtype=int)
        for k in range(len(X_flat_tree)):
            X_flat = X_flat_tree[k]
            X_flat_len = np.vectorize(len)(X_flat)
            # guess_index = np.where(X_flat_len>1)[0].min()
            # mask = (X_flat_len>1)
            # subset_idx = np.argmin(X_flat_len[mask])
            # guess_index = np.arange(X_flat_len.shape[0])[mask][subset_idx]
            # guess_index = masked_argmin(X_flat_len, 2)
            if m<=4:
                mask = (X_flat_len>1)
                subset_idx = np.argmin(X_flat_len[mask])
                guess_index = np.arange(X_flat_len.shape[0])[mask][subset_idx]
            else:
                guess_index = np.where(X_flat_len>1)[0].min()
            

            for guess in X_flat[guess_index]:
                X_flat_tmp = X_flat.copy()
                X_flat_tmp[guess_index] = {guess}
                X_flat_tmp = np.array([X_flat_tmp])
                X_flat_newtree = np.concatenate([X_flat_newtree, X_flat_tmp])
                new_solved_indices_newtree = np.concatenate([new_solved_indices_newtree, np.array([[guess_index]])])
        
        X_flat_tree = np.delete(X_flat_newtree, [0], axis=0)
        new_solved_indices_tree = np.delete(new_solved_indices_newtree, [0], axis=0)
   