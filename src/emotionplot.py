import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns

def plot_result(result, N=1):    
    fig = plt.figure(figsize=(12, 3))
    
    cols_1 = ['char1_sent1_valence', 'char1_sent1_arousal',
        'char1_sent2_valence', 'char1_sent2_arousal',
        'char1_sent3_valence', 'char1_sent3_arousal',
        'char1_sent4_valence', 'char1_sent4_arousal',
        'char1_sent5_valence', 'char1_sent5_arousal']
    
    cols_2 = ['char2_sent1_valence', 'char2_sent1_arousal',
        'char2_sent2_valence', 'char2_sent2_arousal',
        'char2_sent3_valence', 'char2_sent3_arousal',
        'char2_sent4_valence', 'char2_sent4_arousal',
        'char2_sent5_valence', 'char2_sent5_arousal']
    
    cols_r = ['reader_sent1_valence', 'reader_sent1_arousal',
        'reader_sent2_valence', 'reader_sent2_arousal',
        'reader_sent3_valence', 'reader_sent3_arousal',
        'reader_sent4_valence', 'reader_sent4_arousal',
        'reader_sent5_valence', 'reader_sent5_arousal']
            
    char1_array = result.loc[:, cols_1].values.reshape(5,2)
    char2_array = result.loc[:, cols_2].values.reshape(5,2)
    reader_array = result.loc[:, cols_r].values.reshape(5,2)
        
    def plot_array(result_array, ax, title=None):
        for i in range(5):
            if i == 0:
                plt.scatter(result_array[i][0], result_array[i][1], s=30, c="r", marker='s')
            elif i != 4:
                plt.scatter(result_array[i][0], result_array[i][1], s=30, c="b", marker='+')
                arrow = patches.FancyArrowPatch(result_array[i-1], result_array[i],
                                                arrowstyle='->', linestyle='--',
                                                mutation_scale=20)
                ax.add_patch(arrow)
            else:
                plt.scatter(result_array[i][0], result_array[i][1], s=30, c="g", marker="o")
                arrow = patches.FancyArrowPatch(result_array[i-1], result_array[i],
                                                arrowstyle='->', linestyle='--',
                                                mutation_scale=20)
                ax.add_patch(arrow)
                

            plt.xlim(-4.5, 4.5)
            plt.ylim(-4.5, 4.5)
            plt.xlabel("Valence", fontsize='12')
            plt.ylabel("Arousal", fontsize='12')
            
            if title != None:
                plt.title(title, fontsize='15')
        
    ax1 = fig.add_subplot(N, 3, 1, aspect='equal')
    plot_array(char1_array, ax1, "Character 1")
    ax1.grid()
    
    ax2 = fig.add_subplot(N, 3, 2, aspect='equal')
    plot_array(char2_array, ax2, "Character 2")
    ax2.grid()
    
    ax3 = fig.add_subplot(N, 3, 3, aspect='equal')
    plot_array(reader_array, ax3, "Reader")    
    ax3.grid()
    
    return fig


def print_info(result):
    print("Story ID:", result.loc[:, "story_id"].values[0])
    print("Type:", result.loc[:, "type"].values[0])
    print("Rating:", result.loc[:, "rating"].values[0])
    print("Review:", result.loc[:, "Review"].values[0])
