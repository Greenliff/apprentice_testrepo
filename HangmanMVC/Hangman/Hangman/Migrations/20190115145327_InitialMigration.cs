using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace Hangman.Migrations
{
    public partial class InitialMigration : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Languages",
                columns: table => new
                {
                    LanguageId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    LanguageName = table.Column<string>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Languages", x => x.LanguageId);
                });

            migrationBuilder.CreateTable(
                name: "Users",
                columns: table => new
                {
                    UserId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Username = table.Column<string>(nullable: false),
                    Password = table.Column<string>(nullable: false),
                    Mail = table.Column<string>(nullable: false),
                    IsAdmin = table.Column<bool>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Users", x => x.UserId);
                });

            migrationBuilder.CreateTable(
                name: "LetterInfos",
                columns: table => new
                {
                    LetterId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Letter = table.Column<char>(nullable: false),
                    LanguageId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_LetterInfos", x => x.LetterId);
                    table.ForeignKey(
                        name: "FK_LetterInfos_Languages_LanguageId",
                        column: x => x.LanguageId,
                        principalTable: "Languages",
                        principalColumn: "LanguageId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "Games",
                columns: table => new
                {
                    GameId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Date = table.Column<DateTime>(nullable: false),
                    TriesLeft = table.Column<int>(nullable: false),
                    LanguageId = table.Column<int>(nullable: false),
                    UserId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Games", x => x.GameId);
                    table.ForeignKey(
                        name: "FK_Games_Languages_LanguageId",
                        column: x => x.LanguageId,
                        principalTable: "Languages",
                        principalColumn: "LanguageId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_Games_Users_UserId",
                        column: x => x.UserId,
                        principalTable: "Users",
                        principalColumn: "UserId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "WordInfos",
                columns: table => new
                {
                    WordId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Word = table.Column<string>(nullable: false),
                    IsApproved = table.Column<bool>(nullable: false),
                    DateSubmitted = table.Column<DateTime>(nullable: false),
                    SubmitterId = table.Column<int>(nullable: false),
                    LanguageId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_WordInfos", x => x.WordId);
                    table.ForeignKey(
                        name: "FK_WordInfos_Languages_LanguageId",
                        column: x => x.LanguageId,
                        principalTable: "Languages",
                        principalColumn: "LanguageId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_WordInfos_Users_SubmitterId",
                        column: x => x.SubmitterId,
                        principalTable: "Users",
                        principalColumn: "UserId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "WordApprovals",
                columns: table => new
                {
                    WordApprovalId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Date = table.Column<DateTime>(nullable: false),
                    WordId = table.Column<int>(nullable: false),
                    UserId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_WordApprovals", x => x.WordApprovalId);
                    table.ForeignKey(
                        name: "FK_WordApprovals_Users_UserId",
                        column: x => x.UserId,
                        principalTable: "Users",
                        principalColumn: "UserId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_WordApprovals_WordInfos_WordId",
                        column: x => x.WordId,
                        principalTable: "WordInfos",
                        principalColumn: "WordId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "WordsInGame",
                columns: table => new
                {
                    WordInGameId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    State = table.Column<int>(nullable: false),
                    WordId = table.Column<int>(nullable: false),
                    GameId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_WordsInGame", x => x.WordInGameId);
                    table.ForeignKey(
                        name: "FK_WordsInGame_Games_GameId",
                        column: x => x.GameId,
                        principalTable: "Games",
                        principalColumn: "GameId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_WordsInGame_WordInfos_WordId",
                        column: x => x.WordId,
                        principalTable: "WordInfos",
                        principalColumn: "WordId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "GuessedLetters",
                columns: table => new
                {
                    GuessedLetterId = table.Column<int>(nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    LetterId = table.Column<int>(nullable: false),
                    WordInGameId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_GuessedLetters", x => x.GuessedLetterId);
                    table.ForeignKey(
                        name: "FK_GuessedLetters_LetterInfos_LetterId",
                        column: x => x.LetterId,
                        principalTable: "LetterInfos",
                        principalColumn: "LetterId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_GuessedLetters_WordsInGame_WordInGameId",
                        column: x => x.WordInGameId,
                        principalTable: "WordsInGame",
                        principalColumn: "WordInGameId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_Games_LanguageId",
                table: "Games",
                column: "LanguageId");

            migrationBuilder.CreateIndex(
                name: "IX_Games_UserId",
                table: "Games",
                column: "UserId");

            migrationBuilder.CreateIndex(
                name: "IX_GuessedLetters_LetterId",
                table: "GuessedLetters",
                column: "LetterId");

            migrationBuilder.CreateIndex(
                name: "IX_GuessedLetters_WordInGameId",
                table: "GuessedLetters",
                column: "WordInGameId");

            migrationBuilder.CreateIndex(
                name: "IX_LetterInfos_LanguageId",
                table: "LetterInfos",
                column: "LanguageId");

            migrationBuilder.CreateIndex(
                name: "IX_WordApprovals_UserId",
                table: "WordApprovals",
                column: "UserId");

            migrationBuilder.CreateIndex(
                name: "IX_WordApprovals_WordId",
                table: "WordApprovals",
                column: "WordId");

            migrationBuilder.CreateIndex(
                name: "IX_WordInfos_LanguageId",
                table: "WordInfos",
                column: "LanguageId");

            migrationBuilder.CreateIndex(
                name: "IX_WordInfos_SubmitterId",
                table: "WordInfos",
                column: "SubmitterId");

            migrationBuilder.CreateIndex(
                name: "IX_WordsInGame_GameId",
                table: "WordsInGame",
                column: "GameId");

            migrationBuilder.CreateIndex(
                name: "IX_WordsInGame_WordId",
                table: "WordsInGame",
                column: "WordId");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "GuessedLetters");

            migrationBuilder.DropTable(
                name: "WordApprovals");

            migrationBuilder.DropTable(
                name: "LetterInfos");

            migrationBuilder.DropTable(
                name: "WordsInGame");

            migrationBuilder.DropTable(
                name: "Games");

            migrationBuilder.DropTable(
                name: "WordInfos");

            migrationBuilder.DropTable(
                name: "Languages");

            migrationBuilder.DropTable(
                name: "Users");
        }
    }
}
