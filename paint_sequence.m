
sequence;
# returns S
pkg load image;
Colors = rand(36, 3);
side = ceil(sqrt(size(S)(2)));
S_square = reshape(postpad(S, side^2), side, side)';
imagesc(S_square);
colormap(Colors);
