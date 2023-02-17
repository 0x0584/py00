#!/bin/zsh
# download conda
CONDAPATH=/goinfre/$USER/miniconda3
rm -rf $CONDAPATH
# if [ test -f $CONDAPATH ]
# then
	curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
	sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $CONDAPATH
	# configure conda
	$CONDAPATH/bin/conda init zsh
	$CONDAPATH/bin/conda config --set auto_activate_base false
	source $HOME/.zshrc
	# create environement
	conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy
	conda info --envs
	conda activate 42AI-$USER
#fi
export PATH=$PATH:$CONDAPATH/bin
