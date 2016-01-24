sequence2;
# returns St with event id and timestamp.

# Making stereotypical sound
tone_step = 1.0095;

base_tone = sin((1:44100)./44100.*440);

# The first time index: 0
# The last time index: 7361074.7
# Scaling to minutes:
minutes = 5;
sample_s = 0.4;
sound = zeros(44100*(minutes*60 + sample_s),1);
timestep = (minutes*60)/7361075;

for ind = 1:length(St)
  note = St(ind,1);
  time = St(ind,2);
  sample_len = floor(44100*sample_s);
  tone = sin((1:sample_len)./44100 .* 2 .* pi .* (440*(tone_step^note))) .* \
    (1 - (1/sample_len) .* (1:sample_len));
  place = floor((timestep*time * 44100)) + 1;
  sound_sample = sound(place:(place+sample_len-1));
  signal = (sound_sample + tone')/2;
  mixed_sound = signal;
  sound(place:(place+sample_len - 1)) = mixed_sound;
endfor

wavwrite(sound, 44100, 'sequence.wav');

soundsc(sound, 44100);
