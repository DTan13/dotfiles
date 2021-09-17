set encoding=UTF-8

set number
set ruler
set exrc
set secure

set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab

" everything leader
let mapleader = ","
noremap <leader>w :w<cr>
noremap <leader>q :q<cr>
noremap <leader>tn :tabn<cr>
noremap <leader>tp :tabp<cr>
noremap <leader>tt :tabnew<cr>
noremap <leader>f :FloatermNew<cr>
noremap <leader>bd :bd<cr>
noremap <leader>% :vsp<cr>
noremap <leader>" :sp<cr>
noremap <leader>n :NERDTreeToggle<cr>
noremap <leader>p :Rg!<cr>
noremap <leader>a :so ~/.config/nvim/init.vim<cr>

" use Alt + {h,j,k,l} from anywhere
tnoremap <A-h> <C-\><C-N><C-w>h
tnoremap <A-j> <C-\><C-N><C-w>j
tnoremap <A-k> <C-\><C-N><C-w>k
tnoremap <A-l> <C-\><C-N><C-w>l
inoremap <A-h> <C-\><C-N><C-w>h
inoremap <A-j> <C-\><C-N><C-w>j
inoremap <A-k> <C-\><C-N><C-w>k
inoremap <A-l> <C-\><C-N><C-w>l
nnoremap <A-h> <C-w>h
nnoremap <A-j> <C-w>j
nnoremap <A-k> <C-w>k
nnoremap <A-l> <C-w>l

