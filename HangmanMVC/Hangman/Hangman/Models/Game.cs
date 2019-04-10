using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Hangman.Models
{
    public class Game
    {
        [Key]
        public int GameId { get; set; }

        [Required]
        public DateTime Date { get; set; }

        [Required]
        public int TriesLeft { get; set; }

        [Required]
        public int LanguageId { get; set; }

        public Language Language { get; set; }

        [Required]
        public int UserId { get; set; }

        public User User { get; set; }

        public ICollection<WordInGame> WordsInGame { get; set; }
    }
}
